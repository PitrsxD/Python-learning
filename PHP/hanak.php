<?php
/**
 * Template for show Product detail
 *
 * This is the template that displays all pages by default.
 * Please note that this is the WordPress construct of pages
 * and that other 'pages' on your WordPress site will use a
 * different template.
 *
 * @package hanak-forum
 */

get_header();

the_post();
?>

	<?php get_template_part( 'part/hero' ); ?>

	<div class="main">
		<div class="row row--narrow">
			<h1 class="center"><?php the_title(); ?></h1>

			<?php
				if ( $post->post_parent ) {
					$ancestors = get_post_ancestors( $post->ID );
					$root = count($ancestors)-1;
					if ( count($root) > 1 ) {
						$parent = $ancestors[$root];
					} else {
						$parent = -1;
					}
				} else {
					$parent = $post->ID;
				}

				$args = array(
					'posts_per_page' => 20,
					'post_type' => 'sk_products',
					'post_parent' => $parent,
					'orderby' => 'menu_order',
					'order' => 'ASC',
					'no_found_rows' => true,
					'supress_filters' => false,
					'ignore_sticky_posts' => true,
					'post_status' => 'publish'
				);
				$subpages = new WP_Query( $args );
				if ( $subpages->have_posts() ) {
				?>

				<div class="c-main u-full">
					<div class="row row--main">
						<ul class="grid c-main__list">

						<?php
							foreach ( $subpages->posts as $page ) {
								$page_title = get_the_title( $page->ID );
								$thumb_id = get_post_thumbnail_id( $page->ID );
								if ( !empty( $thumb_id ) ) {
									$img = wp_get_attachment_image_src( $thumb_id, 'thumbnail' );
								}
						?>

						<li class="grid__cell size--t-6-12 size--d-4-12 c-main__item">
							<a href="<?php echo get_permalink( $page->ID ); ?>" class="b-main">
								<?php if ( !empty( $thumb_id ) ) : ?>
								<div class="b-main__image" style="background-image: url(<?php echo $img[0]; ?>);"></div>
								<?php endif; ?>
								<div class="b-main__content">
									<h2 class="b-main__name"><?php echo $page->post_title; ?></h2>
									<?php /* ?>
									<p class="b-main__subs">
										<span class="b-main__sub">Moderní kuchyně</span>
									</p>
									<?php */ ?>
								</div>
							</a>
						</li>

						<?php
							}
						?>

						</ul>
					</div>
				</div>

				<?php
				}
				wp_reset_postdata();
			?>

			<?php the_content(); ?>
		</div>

		<?php get_template_part( 'part/about' ); ?>

	</div>

<?php get_footer(); ?>
